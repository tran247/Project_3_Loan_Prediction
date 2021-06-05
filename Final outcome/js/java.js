var depends= [0,1,2,3];
var loan_term=[120,240,360];
var credit= ['Select 1 for credit >= 650 and 0 for > 650',0,1];
var area= ['Select 0 for Semiurban, 1 for Urban and 2 for Rural',0,1,2];
var gender= ['Select 0 for Female and 1 for Male',0,1];
var status= ['Select 0 for No and 1 for Yes',0,1];
var emp= ['Select 0 for No and 1 for Yes',0,1];
for (var i=0; i< depends.length; i++){
       
        
    d3.select('#depend').append('option').text(depends[i]).property('value',depends[i]);
   
  };
for (var i=0; i< loan_term.length; i++){
       
        
    d3.select('#term').append('option').text(loan_term[i]);
   
}; 
for (var i=0; i< credit.length; i++){
       
        
  d3.select('#credit').append('option').text(credit[i]);
 
};
for (var i=0; i< area.length; i++){
       
        
  d3.select('#area').append('option').text(area[i]);
 
};
for (var i=0; i< gender.length; i++){
       
        
  d3.select('#gender').append('option').text(gender[i]);
 
};
for (var i=0; i< status.length; i++){
       
        
  d3.select('#marital').append('option').text(status[i]);
 
};
for (var i=0; i< emp.length; i++){
       
        
  d3.select('#employed').append('option').text(emp[i]);
 
};
   


// console.log(depends)  