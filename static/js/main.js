$( document ).ready(function () {
	let tr=[],checks=[],table=$("#table"),
	count=table.find('tr').length-1,total=0,click=0,datefirst=0,datelast=new Date().getUTCDate();


	for (let i =1;i<=count;i++) {
		checks.push($("#check"+i));
		tr.push($("#td"+i))
	}	

	function dateCompare () {
		let d1=tr[index][0].cells[1].innerHTML,
			datefirst=d1.split('-')[0];

		return datefirst < datelast;
	}

	for (var i = 0; i < checks.length; i++) {
		checks[i].click(function () {
			let index=$(this).attr('name').replace('td','')-1;
			let dinero=tr[index][0].cells[2].innerHTML.replace('$',''),
				d1=tr[index][0].cells[1].innerHTML;

			
			if($(this).is(':checked')){
				click++;
				
				if(click==1 && ((datefirst< datelast) || (datefirst==datelast))){
					date1.innerHTML=d1;
					datefirst=d1.split('-')[0];
						date1.innerHTML=d1.replace(datefirst,datelast);
					console.log(datefirst)

				}else if(click==1){
					datelast=d1.split('-')[0];
					date2.innerHTML=d1;
				}

				if(click==2 && ((datelast > datefirst) || (datelast==datefirst))){
					datelast=d1.split('-')[0];
					date2.innerHTML=d1;
					date1.innerHTML=d1.replace(datelast,datefirst);
					console.log(datelast)
				}else if(click==2){
					datefirst=d1.split('-')[0];
					date1.innerHTML=d1;
				}
				total+=parseFloat(dinero);
			}else{
				click--;
				if(click==1){date2.innerHTML='X/X/X';}
				else if(click==0){date1.innerHTML='X/X/X';}
				total-=parseFloat(dinero);
			}
			income.innerHTML=total;
		});
	}


	//console.log(tr[0][0].cells[2].innerHTML.replace('$',''));	
	

});