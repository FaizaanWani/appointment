$(function(){
    var $select = $(".age_js");
    for (i=1;i<=100;i++){
        $select.append($('<option></option>').val(i).html(i))
    }
})