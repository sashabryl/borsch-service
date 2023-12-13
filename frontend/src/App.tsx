import React from "react";
import {
    Routes,
    Route,
    Outlet,
  } from 'react-router-dom';
import { Header } from "./components/pageComponents/Header/Header.tsx";
import { MainPage } from "./components/page/MainPage/MainPage.tsx";
import "./App.scss"
import { Footer } from "./components/pageComponents/Footer/Footer.tsx";

  const OutletPage = () => {
    return (
      <div className="page">
        <Header />
  
        <Outlet />

        <Footer />
      </div>
    );
  };

export const App = () => {
    return (
        <Routes>
            <Route 
              path="/" 
              element={(
                <OutletPage />
              )}
            >

            <Route 
              index
              element={(
                <MainPage />
              )}
            />
            </Route>

        </Routes>
    );
}
