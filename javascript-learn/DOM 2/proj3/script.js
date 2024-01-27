const courses = [
    {
        name: "Complete ReactJs course",
        price: "2.3"
    },
    {
        name: "Complete Angular course",
        price: "2.1"
    },
    {
        name: "Complete MERN course",
        price: "2.7"
    },
    {
        name: "Complete C++ course",
        price: "2.6"
    },
    {
        name: "Django course",
        price: "7.4"
    },
]


/*The class is always a list 
so that you can use multiple css properties */

function generateLIST(){
    const ul = document.querySelector(".list-group");
    ul.innerHTML = "" ;
    courses.forEach( (course) => {
        const li = document.createElement("li");
        li.classList.add("list-group-item");

        const name = document.createTextNode(course.name);
        li.appendChild(name);

        const span = document.createElement("span");
        span.classList.add("float-right");
        const price = document.createTextNode("$" + course.price);
        span.appendChild(price);

        li.appendChild(span)
        ul.appendChild(li)

    });
}
/*The html tag represents one element and 
the main text inside the html element is called Text node*/
// generateLIST();

window.addEventListener("load", generateLIST);

const button = document.querySelector(".sort-btn")

button.addEventListener("click", () => {
    courses.sort((a,b)=> a.price - b.price)
    generateLIST();
});
// This is a more preferred way where we load the objects
// when the window loads by passing a reference of our function

