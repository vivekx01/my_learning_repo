import React from "react";
import Navbar from "./Navbar";
import HeroSection from "./HeroSection";
import Appsection from "./Appsection";
import Cardsection from "./Cardsection";
import Footer from "./Footer"


const App= () =>{
    return(
        <div>
            <Navbar></Navbar>
            <HeroSection></HeroSection>
            <Appsection></Appsection>
            <Cardsection></Cardsection>
            <Footer></Footer>
        </div>
    )
}

export default App