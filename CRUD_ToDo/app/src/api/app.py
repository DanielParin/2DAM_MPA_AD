from flask import Flask, jsonify, request
import  src.Managers.DatabaseManager as dbm



app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True




@app.route("/")
def main():
    db = dbm.mongo_connect().notesDatabase
    return jsonify({"status": dbm.test_mongodb_connection(db)})



@app.route("/notes", methods=["GET"])
def find_all_notes():
    db = dbm.mongo_connect().noteDatabase

    notes =  list(dbm.find_all(db))
    return jsonify({"notes":notes})



@app.route("/notes", methods=["POST"])
def create_note():
    db = dbm.mongo_connect().noteDatabase

    note = request.json
    created_note = dbm.create_note(db,note)

    return jsonify({"note":create_note})



@app.route("/notes/<id_note>", methods=["GET"])
def find_note(id_note):
    db = dbm.mongo_connect().noteDatabase

    try:
        note = dbm.find_note(db,id_note)
    except ValueError:
        return jsonify({"error":"ID not found"})

    return jsonify({"note":note})



@app.route("/notes/<id_note>", methods=["PUT"])
def update_note(id_note):
    db = dbm.mongo_connect().noteDatabase

    note = request.json
    updated_note = dbm.update_note(db,id_note,note)

    return jsonify({"updatedNote":update_note})



@app.route("/notes/<id_note>", methods=["DELETE"])
def delete_note(id_note):
    db = dbm.mongo_connect().noteDatabase

    deleted_note = dbm.delete_note(db,id_note)

    return jsonify({"deletedNote":deleted_note})