import http from 'http';

const data = JSON.stringify({
    "attributes":[
        "name",
        "age",
        "gender"
    ]
})
console.log(data)
const options = {
  hostname: '192.168.0.5',
  port:5555,
  path: '/create-table',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    "Content-Body":data,
    "key":"wCc93ZH5t5xGwJa0hNJZCg",
    "database":"authdata",
    "table":"vaccination_auth2"
  },
  body:data
};

const getPosts = () => {
  let data = '';

  const request = http.request(options, (response) => {
    // Set the encoding, so we don't get log to the console a bunch of gibberish binary data
    response.setEncoding('utf8');

    // As data starts streaming in, add each chunk to "data"
    response.on('data', (chunk) => {
      data += chunk;
    });

    // The whole response has been received. Print out the result.
    response.on('end', () => {
      console.log("data",data);
    });
  });

  // Log errors if any occur
  request.on('error', (error) => {
    console.error("error",error);
  });

  // End the request
  request.end();
};

getPosts();