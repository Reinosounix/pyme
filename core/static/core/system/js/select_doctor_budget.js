$(document).ready(function(){    
    $("#id_center").change(function(){
        $("#centerId").val($("#id_center").val());
        $("#id_speciality").val(0);   
        $("#id_doctor").val(0);                            
        $("#id_speciality").focus();
        })
        
    $("#id_speciality").change(function(){
        $("#id_speciality").focus();
        $("#speciality").val($("#id_speciality").val());
        $.ajax({
            url: $("#search-select2").attr('action'),
            type: $("#search-select2").attr('method'),            
            data: $("#search-select2").serialize(),   
            dataType: 'json',
            success: function(data){
            console.log(data);         
                var selector='<select><option value="">Seleccione Odontólogo</option>';   
                var val1 = 0;       
                if (data.length == 0){
                    $selector='<option value="">No Existe Odontólogo</option>'
                    }
                else{
                    for (var i=0; i<data.length;i++){
                        selector +='<option value="'+data[i].id+'">'+data[i].name+'</option>';
                        }                      
                    val1 = data[0].id;                        
                    }
                selector+="</select>";  
                $("#doctor").val(val1);                    
                $("#id_doctor").html(selector);
                    },
            error: function(err){
                var selector='<select><option value="">Seleccione Odontólogo</option></select>';
                $("#id_doctor").html(selector);
                $("#speciality").val(0);
                $("#doctor").val(0);
                }
            })
        }) 

    $("#id_doctor").change(function(){
        $("#doctor").val($("#id_doctor").val());
        })

    })