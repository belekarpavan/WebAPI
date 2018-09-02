function validmobile(num) {


    var val=num.value;
    val=val.replace(/\D/g,'');
    num.value=val;

}


function validateemail(textbox)
{
var x=document.getElementById('email').value;
var atposition=x.indexOf("@");
var dotposition=x.lastIndexOf(".");
if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x.length){
    textbox.setCustomValidity('please enter a valid email address');
    return false;
  }
  else
{          textbox.setCustomValidity("");
     return true;
}
}
function validname(name) {

    var val=name.value;
     //alert(val.replace(/\d+/g,''))
    val=val.replace(/\d+/g,'');
    name.value=val;
}

function validpassword() {

    var strength = document.getElementById('strength');

    var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
    var mediumRegex = new RegExp("^(?=.{6,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
    var enoughRegex = new RegExp("(?=.{6,}).*", "g");
    var pwd = document.getElementById("password");


    if (pwd.value.length==0) {
        strength.innerHTML = 'Type Password';
    }
     else if (strongRegex.test(pwd.value)) {
        strength.innerHTML = "<span style='color:green'>Strong!</span>";
    }
    else if (mediumRegex.test(pwd.value)) {
        strength.innerHTML = "<span style='color:orange'>Medium!</span>";
    }
     else if (false == enoughRegex.test(pwd.value)) {
        strength.innerHTML = "More Characters";
    }

    else {
        strength.innerHTML = "<span style='color:red'>Weak!</span>";
    }
}

function getage()
  {

    var udate=document.getElementById('dob').value.substr(0,4);
    var cdate=new Date().getFullYear();
    document.getElementById('age').value = cdate-udate;

  }


$(document).on('submit','#frm',function (e) {
    e.preventDefault();
    $('#loading').prop('hidden', false);
    $('#card').hide();

    $.ajax({
        method:'post',
        url:'http://127.0.0.1:8000/register_student/',
        data:{
            name: $("#name").val(),
            email: $("#email").val(),
            contact: $("#contact").val(),
             csrfmiddlewaretoken:$('Input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            alert("Done");
             $('#loading').hide();
              $('#msg').text("Form Submitted Succesfully...");
             $('#card').fadeIn('slow');
            console.log(data);
        },
        error: function (data) {

            alert("Error....\n"+data);
            $('#loading').hide();

            $('#msg').text("Failed To Submit!");

             $('#card').fadeIn('slow');
            console.log(data);
        }

    });
    $('#frm')[0].reset();
    setTimeout(function () {$('#msg').hide();
    },5000);

});


//****************************Update Form Function**********************************

function loaddata() {
         $.ajax({
        method:'GET',
        url:'http://127.0.0.1:8000/register_student/',
        data:{
             csrfmiddlewaretoken:$('Input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
           // alert("Done");
            console.log(data);

           for(i in data)
           {


                $('#table_body').append("<tr><td>"+data[i].roll+"</td><td>"+data[i].name+"</td><td>"+data[i].email+"</td><td>"+data[i].contact+"</td><td><button class='btn btn-danger' value="+ data[i].roll + " onclick='del(this)' >Delete</button></td><td><button class='btn btn-success' value="+ data[i].roll + " onclick='updt(this)' >Update</button></td></tr>");
           }

        },
        error: function (data) {

            alert("Error....\n");
            console.log(data);
        }

    });

    }





function del(btn) {

    var val=btn.value;
    $.ajax({

       type:'DELETE',
       url:'http://127.0.0.1:8000/register_student/'+val,
       data: {roll:val,
           csrfmiddlewaretoken:$('Input[name=csrfmiddlewaretoken]').val(),
        },
       success:function (data) {
           //alert("Done....");
           $('#table_body').empty();
           loaddata();
           console.log(data);
       } ,
        error:function (data) {
            alert("Fail....\n"+data);
           console.log(data);

        }
    });
}

function updt(btn) {

    var val=btn.value;
    //alert("Update value = "+val);

   $.ajax({

       type:'GET',
       url:'http://127.0.0.1:8000/register_student/'+val,
       data: {roll:val,
           csrfmiddlewaretoken:$('Input[name=csrfmiddlewaretoken]').val(),
        },
       success:function (data) {
          // alert("Done....\n"+data);
           $('#roll').val(data.roll);
           $('#name').val(data.name);
           $('#email').val(data.email);
           $('#contact').val(data.contact);
           $('#myModal').show();
             $('#record').hide();

           console.log(data);
       } ,
        error:function (data) {
            alert("Fail....\n"+data);
           console.log(data);
        }
    });
}

$(document).on('submit','#updfrm',function (e) {
        e.preventDefault();
         var pk=$("#roll").val();
     $.ajax({
       type:'PUT',
       url:'http://127.0.0.1:8000/register_student/'+pk,
       data: {name: $("#name").val(),
              email: $("#email").val(),
              contact: $("#contact").val(),
             csrfmiddlewaretoken:$('Input[name=csrfmiddlewaretoken]').val(),
        },
       success:function (data) {
           alert("Record Updated Successfully....");
             $('#table_body').empty();
                loaddata();
           $('#myModal').hide();
             $('#record').show();

           console.log(data);
       } ,
        error:function (data) {
            alert("Fail....\n"+data);
           console.log(data);

        }
    });

    });

function closefrm() {
    $('#myModal').hide();
    $('#record').show();

}
