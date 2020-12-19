{% extends 'home/base.html' %}
{% block title %} Blogpost{% endblock title %}
{% block body %}
{% load humanize %}
<div class="container my-3">
    <h2 class="blog-post-title">{{post.title}}</h2>
    <p class="blog-post-meta">{{post.timeStamp}} by <a href="/about">{{post.author}}</a></p>
    <p>{{post.content}}</p>
    <hr>
</div>
<div class='container'>
<h5>comments({{comments.count}})</h5>
<div class="my-2">
    {% if user.is_authenticated %}
    <form action="/blog/postComment" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label for="exampleInputEmail1">Post Comment </label>
            <input type="text" class="form-control" name="comment" placeholder="Enter comment here">
        </div>
        <input type="hidden" name="postSno" value="{{post.sno}}">
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    {% else %}
    Please login to post a comment 
    {% endif %}
    </div>
    {% for comment in comments %}
    <div class="row my-3">
        <div class="col-2 col-sm-1 col-md-1 ">
        <img class="rounded mx-auto d-block p-2" style='width:50px;'src="/static/img/user.png"  alt="user">
        </div>
        <div class="col-10 col-sm-11 col-md-11 "> 
        <b> {{comment.user.username}} </b><span class='badge badge-primary'> * {{comment.timestamp| naturaltime}}</span>
        <div> {{comment.comment}} </div>
    </div>
    </div>
    {% endfor %}

    
</div>
{% endblock %}