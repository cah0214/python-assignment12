import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("db/lesson.db")

query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

employee_results = pd.read_sql_query(query, conn)
conn.close()

ax = employee_results.plot(
    kind="bar",
    x="last_name",
    y="revenue",
    legend=False,
    title="Revenue by Employee"
)

ax.set_xlabel("Employee Last Name")
ax.set_ylabel("Revenue ($)")
plt.tight_layout()
plt.show() 
