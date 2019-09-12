$(document).ready(function(){    
    $("#id_date").blur(function(){
        $.ajax({
            url: $("#search-schedule").attr('action'),
            type: $("#search-schedule").attr('method'),            
            data: $("#search-schedule").serialize(),   
            dataType: 'json',
            beforeSend: function(xhr){xhr.setRequestHeader('X-CSRFToken', "{{csrf_token}}");},
            success: function(data){
                //console.log(data);
               var user_name=$("#user_name").val();            
                var cadena="";          
                if (data.length == 0){
                    $cadena='<p>No existen horarios disponibles para esta fecha</p>'
                    }
                else{
                    for (var i=0; i<data.length;i++){
                        msj = " Desde las "+data[i].start+" Hasta las "+data[i].final;
                        cadena +='<form action="/ext_schedule_saved/" method="post"><input type="hidden" name="id" value="'+data[i].id+'"/><input type="hidden" name="user_name" value="'+user_name+'"/><div class="row"><div class="col-12 col-sm-8 mb-3"><input type="text" class="form-control" value="'+msj+'"/></div><div class="col-12 col-sm-4 mb-3"><input type="submit" value="Agendar" class="btn btn-primary form-control"></div></div></form><hr>';
                        }
                    }
                $("#horarios").html(cadena);
                },
            error: function(err){
                alert("Error");
                }
            })
    
        })
    })