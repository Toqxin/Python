const sql = require('mssql/msnodesqlv8');
const express = require('express');
const app = express();
const port = 3000;

//API key
const apiKeys = ['10fgfdgj85k34kspay64f'];//This is an example of API key, not real

//API key control
app.use((req, res, next) => {
    const apiKey = req.get('py_apiKey');
    if (apiKeys.includes(apiKey)) {
        next();
    } else {
        res.status(403).send({error: 'Api key is incorrect.'});
    }
});

//Configuration of connecting to database
const config = {
    server: 'SERVER_NAME', 
    database: 'DATABASE_NAME',
    driver: 'msnodesqlv8',
    options: {
        trustedConnection: true
    }
};

//Attracts features of designated cars
app.get('/api/cars/:brand', async (req, res) => {
    try {
        let pool = await sql.connect(config)
        let result = await pool.request()
            .input('input_parameter', sql.VarChar, req.params.brand)
            .query('SELECT * from Cars WHERE Brand = @input_parameter')

        res.json(result.recordset);
    } catch (err) {
        console.error(err);
        res.status(500).send({error: 'Database Error'});
    }
});

//Connects to Sql server and retrieves all data of the relevant table
app.get('/api/cars', async (req, res) => {
    try {
        let pool = await sql.connect(config)
        let result = await pool.request()
            .query('SELECT * from Cars')

        res.json(result.recordset);
    } catch (err) {
        console.error(err);
        res.status(500).send({error: 'Database Error'});
    }
});

//Port 3000 is being listened
app.listen(port, () => {
    console.log(`App running on http://localhost:${port}`)
});
