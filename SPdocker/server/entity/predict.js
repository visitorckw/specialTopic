var EntitySchema = require("typeorm").EntitySchema;

module.exports = new EntitySchema({
    name: "predict", // Will use table name `post` as default behaviour.
    tableName: "predict", // Optional: Provide `tableName` property to override the default behaviour for table name. 
    columns: {
        gameId: {
        	primary: true,
            type: "int",
        },
        result: {
        	type: "varchar",
        }
    }
});


// pid account passWord games scores

// gameId pid date scores
