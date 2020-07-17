import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import './App.css';
import GetVehicleTable from './components/homeTable'

function App(props) {
  return (
    <div >
      <Router>
      
        <Switch>
          <Route path="/">
            <GetVehicleTable {...props} />
          </Route>
        </Switch>
    </Router>

    </div>
  );
}

export default App;
