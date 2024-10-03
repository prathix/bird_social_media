document.addEventListener("DOMContentLoaded", function() {

    let post = document.querySelectorAll(".post")
    function distance(post) {
            let margin = 100; // Desired margin between the posts
    
            // Ensure all posts have absolute positioning
            post.forEach((currentPost, index) => {
            currentPost.style.position = 'absolute';
            if (index > 0) {
                let previousPost = post[index - 1];
                // Position the current post based on the previous post plus the margin
                currentPost.style.top = (previousPost.offsetTop + previousPost.offsetHeight + margin) + 'px';
            } else {
                // Position the first post at the start
                currentPost.style.top = '100px';
            }
        });
    }

});