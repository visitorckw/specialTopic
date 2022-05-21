var EntitySchema = require("typeorm").EntitySchema;

module.exports = new EntitySchema({
    name: "game", // Will use table name `post` as default behaviour.
    tableName: "game", // Optional: Provide `tableName` property to override the default behaviour for table name. 
    columns: {
        gameId: {
            primary: true,
            type: "int",
            generated: true
        },
        pid: {
            type: "int"
        },
        date: {
            type: "varchar"
        },
        mode: {
            type: "varchar"
        },
        score: {
        	type: "int"
        }
    }
});


// pid account passWord games scores

// gameId pid date scores
