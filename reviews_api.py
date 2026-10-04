"""
reviews api - read from the reviews table in store.db and return
aggregated reviews information for a given product
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "store.db")

def get_product_rating(product_id: int) -> dict:
    """Return avg rating and review count for a single product"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT AVG(rating), COUNT(*) FROM reviews WHERE product_id = ?",
        (product_id,)
    )
    row = cursor.fetchone()
    conn.close()

    avg = round(row[0], 2) if row[0] is not None else 0.0
    count = row[1] if row else 0
    return{"product_id": product_id, "average_rating": avg, "review_count": count}

"""Return ratings for a list of product ids"""
def get_product_ratings(product_ids: list[int]) -> list[dict]:
    if not product_ids:
        return []
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    placeholders = ','.join('?' for _ in product_ids)
    cursor.execute(
        f"""
        SELECT product_id, AVG(rating), COUNT(*)
        FROM reviews
        WHERE product_id IN ({placeholders})
        GROUP BY product_id
        """,
        product_ids
    )
    rows = cursor.fetchall()
    conn.close()

    rating_map = {
        r[0]: 
        {"average_rating": round(r[1], 2), 
        "review_count": r[2]
        } 
        for r in rows
        }

    return[
        {
            "product_id": pid,
            "average_rating": rating_map.get(pid, {}).get("average_rating", 0.0),
            "review_count": rating_map.get(pid, {}).get("review_count", 0)
        }
        for pid in product_ids
    ]

if __name__ == "__main__":
    #single product
    result = get_product_rating(2)
    print("single product rating:")
    print(f" Product {result['product_id']} : "
          f"{result['average_rating']} stars " 
          f"({result['review_count']} reviews)")

    #multiple products
    print("\n Batch ratings:")
    results = get_product_ratings([1, 3, 2, 7])
    for r in results:
        print(f" Product {r['product_id']} : "
              f"{r['average_rating']} stars " 
              f"({r['review_count']} reviews)")