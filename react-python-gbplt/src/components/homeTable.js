import React, {useState,useEffect} from 'react';
import { Table } from 'semantic-ui-react';
import '../style/HomePage.css';
import {gqlpromise} from '../services/gqlService';
function GetVehicleTable(props){
    const [TableData,setTableData] = useState();
    const [RefreshTable, setRefreshTable] = useState(true);
    useEffect(() => {
        let params = `
            query PostsForAuthor {
                allEmployees{
                  edges{
                    node{
                      VEHICLEMake
                      VEHICLEModel
                      VEHICLETagNum
                    }
                  }
                }
              } 
        `
        gqlpromise(params).then((resp) => {
            setTableData(resp);
        });
    }, [RefreshTable])
    
    return(
        <div className = "MainContainer">
            <div className = "tableContaner">
                <Table unstackable>
                    <Table.Header>
                    <Table.Row>
                        <Table.HeaderCell>Name</Table.HeaderCell>
                        <Table.HeaderCell>Status</Table.HeaderCell>
                        <Table.HeaderCell textAlign='right'>Notes</Table.HeaderCell>
                    </Table.Row>
                    </Table.Header>

                    <Table.Body>
                        {
                            TableData ? 
                            TableData.edges.map((item, index) => (
                                    <Table.Row key = {index+1}>
                                        <Table.Cell key = {index+2}>{item.node.VEHICLEMake}</Table.Cell>
                                        <Table.Cell key = {index+3}>{item.node.VEHICLEModel}</Table.Cell>
                                        <Table.Cell textAlign='right' key = {index+4}>{item.node.VEHICLETagNum}</Table.Cell>
                                    </Table.Row>
                            )) : undefined
                        }
                    
                    
                    </Table.Body>
                </Table>
            </div>
        </div>
    )
}

export default GetVehicleTable;