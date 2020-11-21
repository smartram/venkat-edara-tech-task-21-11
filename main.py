from flask import Flask, request
import datetime
import json
from chef import Chef


app = Flask(__name__)
manager = Chef()
manager.load_conf()

@app.route("/lunch", methods=["GET"])
def select_lunch():
    now = datetime.datetime.now()
    lunch_date = request.args.get('date', None)
    if lunch_date is None:
        lunch_date = now
    else:
        fields = lunch_date.split("-")
        if len(fields) < 3:
            return "Bad Format of Date", 400
        lunch_date = datetime.datetime(year=int(fields[0]), month=int(fields[1]), day=int(fields[2]))
    list_dishes = manager.filter_dishes(lunch_date)
    return json.dumps({"dishes":list_dishes}, indent=4), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

