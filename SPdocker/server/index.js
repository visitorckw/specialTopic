var express = require('express');
var typeorm = require('typeorm');
const prefix = '/api';


typeorm.createConnection({
    type: "mysql",
    host: "mysql",
    port: 3306,
    username: "visitor",
    password: "visitor",
    database: "myDB",
    synchronize: true,
    entities: [
        require("./entity/user.js"),
        require("./entity/game.js")
    ]
}).then(function(connection){
	console.log('server connect database success');
	console.log('SERVER START LISTEN ON PORT 3000');
	const app = express();
	app.get('/', function(req, res){
		res.send('hello world from nodejs');
	})
	app.get(prefix, function(req, res){
		console.log('An GET request');
	    res.send("hello from api route in node.js");
	})
	app.get(prefix+'/version', function(req, res){
		console.log('version GET');
		res.send({ver: '0.1.0'});
	});
	app.get('/get', function(req, res){
		let params = req.query;
		console.log('params: ', params);
		let obj = {
			account: "visitorckw",
			passWord: "visit",
			games: 10,
			scores: parseInt(params.scores, 10)
		};
		let repo = connection.getRepository('user');
		repo.find().then(function(objres){
			res.send(objres);
		})
	})
	app.get('/set', function(req, res){
		let params = req.query;
		let obj = {
			account: "visitorckw",
			passWord: "visit",
			games: 10,
			scores: parseInt(params.scores, 10)
		};
		let repo = connection.getRepository('user');
		repo.save(obj).then(function(saveOBJ){
			console.log('An object has been saved', saveOBJ);
			//return repo.find();
			res.send(saveOBJ);
		})
	})
	app.get(prefix+'/login', function(req, res){
		let params = req.query;
		let repo = connection.getRepository('user');
		repo.findOne({account: params.account}).then(function(usr){
			if(!usr){
				res.send({pid: -1, status: 1, msg: "account not found"});
			}
			else if(usr.passWord != params.passWord){
				res.send({pid: -1, status: 2, msg: "incorrect password"});
			}
			else{
				res.send({pid: usr.pid, status: 0,nickname: usr.nickname, msg: "login success"});
			}
		});
	});
	app.get(prefix+'/register', function(req, res){
		let params = req.query;
		let repo = connection.getRepository('user');
		repo.findOne({account: params.account}).then(function(usr){
			if(usr){
				res.send({status: 1, msg: "account already exist"});
			}
			else{
				repo.save({
					account: params.account,
					passWord: params.passWord,
					nickname: params.nickname,
					games: 0,
					scores: 0
				}).then(function(obj){
					res.send({status: 0, msg: "register success"});
				})
			}
		});
	});
	app.get(prefix + '/saveGame', function(req, res){
		let params = req.query;
		let repo = connection.getRepository('user');
		repo.findOne({pid: params.pid}).then(function(usr){
			console.log(usr);
			let newGames = usr.games + 1;
			let newScores = usr.scores + params.score;
			let GameRepo = connection.getRepository('game');
			repo.save({
				pid: usr.pid,
				account: usr.account,
				passWord: usr.passWord,
				nickname: usr.nickname,
				games: newGames,
				scores: newScores,
			});
			GameRepo.save({
				pid: usr.pid,
				date: new Date().toString(),
				mode: params.mode,
				score: params.score,
			});
			res.send({status: 0, msg: 'success'});
		});
		// res.send({status: 0, msg: 'success'});
	});
	app.get(prefix + '/games', function(req, res){
		console.log('GET games');
		let params = req.query;
		let repo = connection.getRepository('game');
		let ans = repo.createQueryBuilder("game")
		.where('game.pid=' + params.pid)
		// .orderBy('game.date', 'desc')
  		.getMany();
		res.send(ans);
	});
	app.listen(3000);
}).catch(function(err){
	console.log(err);
})
