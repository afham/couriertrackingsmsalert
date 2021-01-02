
console.log('Hello world df')
var updateBtns = document.getElementsByClassName("updatecontainer")
console.log(updateBtns)


for(var j=0; j<updateBtns.length;j++){
	updateBtns[j].addEventListener('click',function(){

		var current = document.getElementsByClassName("active");

    
	    

 
        this.className += " active";
		var containerId=this.dataset.cont_id;
		var customerId= this.dataset.id;
		var action = this.dataset.action;
		console.log('customerId is ',customerId, 'action is ',action ,'container is',containerId);
		updatecontainerlist(customerId,action,containerId);


	})


}




function updatecontainerlist(customerId,action,containerId){
	console.log('USer logged in and sending data')
	var url='/add_customer/'
	fetch(url,{
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,

		},
		body:JSON.stringify({'customerId':customerId,'action':action,'containerId':containerId})
	})

	.then((response) =>{
		return response.json()
		
	})

	.then((data) =>{
		console.log('data: ',data)
	})
}



