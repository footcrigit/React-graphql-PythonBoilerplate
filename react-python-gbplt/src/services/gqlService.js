import axios from 'axios';

export const gqlpromise = (params) => new Promise(function (resolve,reject ){
    axios({
        url: 'http://127.0.0.1:5000/graphql',
        method: 'post',
        data: {
          query: params
        }
      }).then((result) => {
        resolve(result.data.data.allEmployees)
      });
})
