import React from "react";
import { NavLink } from 'react-router-dom';
import "./Header.scss";

export const Header = () => {
    return (
      <div className="header">
        <div className="header__constainer">
           <NavLink
              to="/"
              className="logo"
            />

            <ul className="header__nav">
                <li>
                    <NavLink 
                      to="/favourites"
                      className="header__nav--link"
                    >
                      Favorites
                    </NavLink>
                </li>

                <li>
                    <NavLink 
                      to="/aboutUs"
                      className="header__nav--link"
                    >
                      About us
                    </NavLink>
                </li>

                <li>
                    <NavLink 
                      to="/contacts"
                      className="header__nav--link"
                    >
                      Contacts
                    </NavLink>
                </li>
            </ul>

            <NavLink
              to="/profile"
              className="header__profile"
            />
          </div>
      </div>
    );
}