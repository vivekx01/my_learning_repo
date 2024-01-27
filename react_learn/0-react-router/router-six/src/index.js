import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, 
  Routes,
  Route,
  Navigate,
  Link,
  Outlet,
  useParams,
  NavLink,
  useNavigate,
  useLocation
} 
  from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <Routes>
      <Route path="/" element={<Home />}></Route>
      <Route path="/myapp" element={<Navigate replace to="/learn" />}></Route>
      <Route path="/learn" element={<Learn />}>
        <Route path="course" element={<Courses/>}>
          <Route path=":courseid" element={<CourseId />}></Route>
        </Route>
        <Route path="bundle" element={<Bundles/>} />
      </Route>
      <Route path='/dashboard' element={<Dashboard></Dashboard>} />
    </Routes>
  </Router>
);

function Home(){
  return (
    <div>
      <h1>Home route</h1>
      <Link to="/learn">Go to Learn</Link>
    </div>
  )
}
function Learn(){
  return (
    <div>
      <h1>Learn</h1>
      <h4>All courses are listed here</h4>
      <Link to="/learn/course">courses</Link> |
      <Link to="/learn/bundle">bundles</Link>
      <Outlet></Outlet>
    </div>
  )
}
function Courses(){
  const courseList = ["React","Angular","Vue","Nodejs"]
  const randomName = courseList[Math.floor(Math.random()* courseList.length)]
  return (
    <div>
      <h1>Courses list</h1>
      <NavLink
      style={({isActive})=>{
        return {
          backgroundColor: isActive ? "pink" : "yellow"
        }
      }} 
       to={`/learn/course/${randomName}`}>{randomName}</NavLink> | 
      <NavLink to={`/learn/course/tests`}>tests</NavLink>
      <Outlet></Outlet>
      
    </div>
  )
}
function Bundles(){
  return (
    <div>
      <h1>Bundles</h1>
    </div>
  )
}
function CourseId(){
  const navigate = useNavigate()
  const {courseid}=useParams()
  return (
    <div>
      <h1>URL params: {courseid} </h1>
      <button onClick={()=>{
        navigate("/dashboard", {state: courseid});
      }}>Price</button>|  
       <Link to="/dashboard" state={"Django"}>test link</Link>
    </div>
  )
}
function Dashboard(){
  const location = useLocation();
  return (
    <div>
      <h1>Info that we got here is {location.state}</h1>
    </div>
  )
}

reportWebVitals();
