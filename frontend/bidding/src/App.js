import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";


function App() {
  const [competitionData, setCompetitionData] = useState([]);
  const AuthStr = 'Token '.concat('d63571d18479c4aa301dd7727c1ec59291d34bc4');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/api/all-competitions-seller-bids/', { headers: { Authorization: AuthStr }})
      .then((res) => {
        setCompetitionData(res.data);
      })
      .catch((err) => console.log(err));
  }, [AuthStr]);

  return (
    <div className="App">

        <center>React Table Demo</center>

        {console.log("competitionData Data", competitionData)}
        
        <table style = {{borderCollapse:"separate"}} class="content-table">
          <thead>
            <td>Buyers</td>
            <td>Competition</td>
            <td>Seller</td>
            <td>Total Bids</td>
          </thead>

          <tbody>
            {competitionData.map((data)=>
              <tr>
                <td>{data["buyer_name"]}</td>
                <td>{data["competition_name"]}</td>
                <td>{data["seller_name"]}</td>
                <td>{data["bids"]}</td>
              </tr>
            )}

          </tbody>

        </table>
    </div>
  );
}

export default App;