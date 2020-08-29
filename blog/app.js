var express = require("express");
var app = express();
var mongoose = require("mongoose");
var bodyparser=require("body-parser");
var methodOverride = require("method-override");

app.use(bodyparser.urlencoded({extended:true}));
mongoose.connect("mongodb+srv://arham:arham@cluster0.dkiwy.mongodb.net/yelpcamp?retryWrites=true&w=majority"  , { useNewUrlParser: true , useUnifiedTopology : true });
app.use(methodOverride("_method"));


// database -----------
//schema 
var blogschema = new mongoose.Schema({
    name : String ,
    image : String ,
    body : String ,
    date : { type : Date , default : Date.now }
});

//creating model
var blogs =  mongoose.model('bogs',blogschema);

//routes ---------------------

app.get("/blogs",function(req,res){
    blogs.find({} , function(err , allBlogs){
        if(err){
            console.log("there is some error, could not find all the blogs from database");
            res.redirect("/error");
        }
        else{
            console.log(allBlogs);
            res.render("index.ejs", {allBlogs:allBlogs} );
        }
    })
   
});

app.get("/blogs/new",function(req,res){
   res.render("new.ejs");
});

app.get("/blogs/:id",function(req,res){
    blogs.findById(req.params.id , function(err , oneBlog){
        if(err){
            console.log("cannot find element with following id");
            console.log(req.params.id);
            res.redirect("/blogs");
        }
        else{
            
             res.render("show.ejs", {blog:oneBlog} ); 
        }
    })
  
});

app.get("/blogs/:id/edit",function(req,res){
   blogs.findById(req.params.id , function(err , oneBlog){
        if(err){
            console.log("cannot find element with following id");
            console.log(req.params.id);
            res.redirect("/blogs");
        }
        else{
            
             res.render("edit.ejs", {blog:oneBlog} ); 
        }
    })
});

app.post("/blogs",function(req,res){
   //console.log(req.body);
   var blog=req.body.blog;
   blogs.create(blog , function(err,newblog){
       if(err){
           console.log("there is some error in adding blog");
           res.redirect("/blogs");
       }
       else{
           console.log("blog added");
           console.log(newblog);
           res.redirect("/blogs");
       }
   });
   
   
  
});

app.put("/blogs/:id", function(req , res ){
    blogs.findOneAndUpdate({ "_id" :req.params.id} , req.body.blog , function(err , updated){
        if(err){
            console.log("could not update blog with following id");
            console.log(req.params.id);
        }
        else{
            console.log("Updated blog");
            console.log(updated);
            res.redirect("/blogs/" + req.params.id);
        }
    });
});

app.delete("/blogs/:id",function(req,res){
    blogs.findByIdAndRemove(req.params.id , function(err){
        if(err){
            console.log("some error in deleting ");
        }
        else{
            console.log("deleted successfuly ");
            res.redirect("/blogs")
        }
    })
});

app.get("/",function(req,res){
   res.redirect("/blogs"); 
});



app.get("/*",function(req,res){
    console.log(req);
   res.send("plz enter correct url"); 
});


//setting server ------------
app.listen( 3000 , function(){
    console.log("server started");
});
