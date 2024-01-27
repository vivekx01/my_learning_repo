import React, { useState } from "react";
import ThemeContext from "./context/ThemeContext";
import Toggler from "./components/Toggler";
import HeroSection from "./components/HeroSection";



const App =()=>{
  const themeHook = useState("light")
  return(
    <ThemeContext.Provider value={themeHook}>
      <div>
        <Toggler></Toggler>
        <HeroSection></HeroSection>
      </div>
    </ThemeContext.Provider>
  )
  
}

export default App;