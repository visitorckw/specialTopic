var EntitySchema = require("typeorm").EntitySchema;

module.exports = new EntitySchema({
    name: "user", // Will use table name `post` as default behaviour.
    tableName: "user", // Optional: Provide `tableName` property to override the default behaviour for table name. 
    columns: {
        pid: {
            primary: true,
            type: "int",
            generated: true
        },
        account: {
            type: "varchar"
        },
        passWord: {
            type: "varchar"
        },
        games: {
        	type: "int"
        },
        scores: {
        	type: "int"
        }
    }
});


// pid account passWord games scores
