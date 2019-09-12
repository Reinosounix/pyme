$(document).ready(function(){    
    $("#id_date").blur(function(){
        $("#search-schedule").submit();
        /*
        $.ajax({
            url: $("#search-schedule").attr('action'),
            type: $("#search-schedule").attr('method'),            
            data: $("#search-schedule").serialize(),   
            dataType: 'json',
            beforeSend: function(xhr){xhr.setRequestHeader('X-CSRFToken', "{{csrf_token}}");},
            success: function(data){
                console.log(data);
                var user_name=$("#user_name").val();            
                var cadena="";          
                if (data.length == 0){
                    cadena+='<tr><td colspan="5">No existen horarios disponibles para esta fecha</td></tr>';
                    console.log(data.length);
                    }
                else{
                    for (var i=0; i<data.length;i++){
                        cadena +='<tr><td><input type="time" class=" form-control border-primary" value="'+data[i].start+'" disabled/></td><td><input type="text" class=" form-control border-primary" value="Estados '+data[i].state+'" disabled/></td>';
                        if ((data[i].state == 'Agendada') || (data[i].state == 'Agendada Online')){ 
                            cadena += '<td><input type="text" class=" form-control border-primary" value="Paciente '+data[i].patient_name+'" disabled/></td>';
                            }    
                        else{
                            cadena += '<td><input type="text" class=" form-control border-primary" value="Sin Paciente" disabled/></td>';                                    
                            }
                        if (data[i].state == 'Libre'){
                            cadena += '<td><a href="/secretary/int_schedule_fromld_rut/'+data[i].id+'/" class="btn btn-primary form-control">Agendar</a></td><td><a href="/secretary/block_fromld_schedules/'+data[i].id+'" class="btn btn-primary form-control">Bloquear</a></td>';                                                   
                            }                                    
                        if (data[i].state == 'Agendada' || data[i].state == 'Agendada Online'){                                    
                            cadena += '<td><a href="/secretary/cancel_schedule_fromld/'+data[i].id+'/" class="btn btn-primary form-control">Cancelar</a></td><td><a href="/secretary/attention_fromld_init/'+data[i].id+'/" class="btn btn-primary form-control">Atender</a></td>';
                            }
                        if (data[i].state == 'Bloqueada'){                                    
                            cadena += '<td><a href="/secretary/activate_fromld_schedule/'+data[i].id+'/" class="btn btn-primary form-control">Activar</a></td>';                                                   
                            }
                        cadena +='</tr>';
                        }
                    }
                $("#horarios").html(cadena);
                },
            error: function(err){
                alert("Error");
                }
            })
    */
        })
    })