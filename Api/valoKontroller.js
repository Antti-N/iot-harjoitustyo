'use strict'

// Asenna ensin mysql driver 
// npm install mysql --save

var mysql = require('mysql');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',  // HUOM! Älä käytä root:n tunnusta tuotantokoneella!!!!
  password : 'moikkajee',
  database : 'liikennevalot'
});

module.exports = 
{

    valot: function(req, res){

        var kysely = "SELECT * FROM valot WHERE id = 1";
        //console.log(req.params);

        var kellot = [];

        connection.query(kysely, (virhe, tulokset, kentat) => {
            if (!virhe) {
                res.send(tulokset)
            } else {
                res.send({"status" : 500, "virhe" : virhe, "response" : null});
            }

        });
    },

}
