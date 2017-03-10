function createTable()
{
    var num_rows = document.getElementById('rows').value;
    var num_cols = document.getElementById('cols').value;
    var theader = '<table border="1" style="border-collapse: separate; border-spacing: 10px;" >\n';
    var tbody = '';
	var drp= '';
	for( var k=0;k<num_cols;k++){
		drp+='<input type="text">'
		drp+='<select id='+k+' onchange="myFun(this.id)"><option select="selected">Select</option><option value="number"+">number</option><option value="text"+">string</option></select></input>'
	}
    for( var i=0; i<num_rows;i++)
    {
        tbody += '<tr>';
        for( var j=0; j<num_cols;j++)
        {
            tbody += '<td>';
            tbody += '<input type="text" name="'+i*10+j+'" id="'+i*10+j+'" required></input>'
            tbody += '</td>'
        }
        tbody += '</tr>\n';
    }
    var tfooter = '</table>';
    document.getElementById('wrapper').innerHTML = drp + theader + tbody + tfooter;
}
function myFun(val) {
var d=document.getElementById(val);
var num_rows = document.getElementById('rows').value;
var sol=d.options[d.selectedIndex].value;
for(var f=0;f<num_rows;f++){
	var g=document.getElementById(f*10+val);
	g.setAttribute("type",String(sol));
}
}