#!/usr/bin/node

const request = require('request');

const exactOrder = (actors, x) => {
    if (!actors || x === actors.length) return; // Check if actors is undefined or if x exceeds its length
    request(actors[x], function (err, res, body) {
        if (err) throw err;
        try {
            const actorName = JSON.parse(body).name;
            console.log(actorName);
        } catch (error) {
            console.error("Error parsing actor data:", error.message);
        }
        exactOrder(actors, x + 1);
    });
};

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
    if (err) throw err;
    try {
        const filmData = JSON.parse(body);
        const actors = filmData.characters;
        exactOrder(actors, 0);
    } catch (error) {
        console.error("Error parsing film data:", error.message);
    }
});
