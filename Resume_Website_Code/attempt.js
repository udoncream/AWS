fetch ('https://sbf6r47lld.execute-api.us-west-1.amazonaws.com/Test/')  
    .then(res => {
        return res.json();
    })
    .then(data => {
        const guestCount= document.getElementById('visitorCount');
        guestCount.innerHTML = data
    });
//test
