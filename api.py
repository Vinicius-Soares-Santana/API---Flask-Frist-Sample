from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, text
from psycopg2.extras import RealDictCursor
import psycopg2


app = Flask(__name__)

CORS(app)




@app.route("/")
def first_answer():
    return jsonify(status = 'ok')


@app.route("/all", methods=["GET"])
def select_all():
    try:
        conn = psycopg2.connect(host = "127.0.0.1", database = "guide", user = "postgres", password="1234")
        with conn.cursor(cursor_factory=RealDictCursor) as my_cursor:
            my_cursor.execute("SELECT * FROM SampleData")
            result = my_cursor.fetchall()
            return jsonify(result), 200
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    finally:
        my_cursor.close()
        conn.close()



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)
