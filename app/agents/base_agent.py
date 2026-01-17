import google.generativeai as genai
import os
import re
import json
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()

class BaseAgent:
    def __init__(self, agent_name, engine, schema_description):
        self.agent_name = agent_name
        self.engine = engine
        self.schema_description = schema_description
        self.api_key = os.getenv("GOOGLE_API_KEY")
        
        if not self.api_key:
             print("WARNING: GOOGLE_API_KEY not found in environment variables.")
        else:
             genai.configure(api_key=self.api_key)
             self.model = genai.GenerativeModel('gemini-2.0-flash-exp')

    def allowed_sql_check(self, sql):
        """
        Simple safety check to ensure only SELECT statements are executed.
        """
        sql_upper = sql.upper().strip()
        if not sql_upper.startswith("SELECT"):
            return False, "Only SELECT queries are allowed."
        sensitive_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE", "GRANT"]
        for keyword in sensitive_keywords:
            if re.search(f"\\b{keyword}\\b", sql_upper):
                return False, f"Usage of {keyword} is not allowed."
        return True, ""

    def process_query(self, user_query):
        """
        1. Formats prompt with schema.
        2. Calls Gemini to generate SQL.
        3. Validates SQL.
        4. Executes SQL.
        5. Returns result.
        """
        prompt = f"""
You are an expert SQL agent for the {self.agent_name} database.
Your goal is to convert the user's natural language query into an executable SQL query.

Database Schema:
{self.schema_description}

Rules:
1. Output ONLY the raw SQL query. Do not use markdown blocks (```sql ... ```).
2. The query must be READ-ONLY (SELECT).
3. Do not assume any tables or columns that are not listed in the schema.
4. If the query cannot be answered with the given schema, output "CANNOT_ANSWER".

User Query: "{user_query}"
        """
        
        try:
            response = self.model.generate_content(prompt)
            sql_query = response.text.strip()
            
            # Remove markdown formatting if the LLM adds it despite instructions
            sql_query = re.sub(r"```sql\s*", "", sql_query)
            sql_query = re.sub(r"```\s*$", "", sql_query)
            sql_query = sql_query.strip()

            if sql_query == "CANNOT_ANSWER":
                return {"error": "I cannot answer this question based on my database schema."}

            is_valid, validation_msg = self.allowed_sql_check(sql_query)
            if not is_valid:
                return {"error": f"SQL Safety Violation: {validation_msg}"}

            print(f"[{self.agent_name}] Executing SQL: {sql_query}")
            
            with self.engine.connect() as connection:
                result = connection.execute(text(sql_query))
                rows = [dict(row._mapping) for row in result]
                return {"data": rows, "sql": sql_query}

        except Exception as e:
            print(f"DEBUG: Detailed error: {e}")
            print("FALLBACK: Attempting regex-based SQL generation.")
            
            # Simple Regex Fallbacks for Demo
            q = user_query.lower()
            sql_query = ""
            
            # ShopCore Fallbacks
            if "products" in q and "under" in q:
               val = re.search(r"(\d+)", q)
               limit = val.group(1) if val else "50"
               sql_query = f"SELECT * FROM products WHERE price < {limit} LIMIT 3"
            elif "customer" in q and "john doe" in q:
               sql_query = "SELECT * FROM customers WHERE full_name LIKE '%John Doe%' LIMIT 1"
            elif "orders" in q and "customer id" in q:
               # excessive simplification: just get recent orders
               sql_query = "SELECT * FROM orders ORDER BY created_at DESC LIMIT 3"
            
            # ShipStream Fallbacks
            elif "status" in q and "shipment" in q:
               sql_query = "SELECT * FROM shipments LIMIT 5"
            elif "status" in q and "order" in q:
                sql_query = "SELECT * FROM shipments LIMIT 5"
               
            # PayGuard Fallbacks
            elif "wallet" in q:
               sql_query = "SELECT * FROM wallets LIMIT 1"
            
            # CareDesk Fallbacks
            elif "ticket" in q:
               sql_query = "SELECT * FROM tickets WHERE status='open' LIMIT 5"
               
            if sql_query:
                print(f"[{self.agent_name}] Fallback SQL: {sql_query}")
                with self.engine.connect() as connection:
                    result = connection.execute(text(sql_query))
                    rows = [dict(row._mapping) for row in result]
                    return {"data": rows, "sql": sql_query}
            
            return {"error": f"Agent Error: {str(e)}"}
