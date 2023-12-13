import React from "react";
import { NavLink } from "react-router-dom";

import "./Footer.scss"

export const Footer = () => {
  const footerArr = [
    'Terms of use',
    'Cookies',
    'Privacy Policy',
    'Legal notice',
  ];
  return (
      <div className="footer">
           <NavLink
              to="/"
              className="logo"
            />

            <div className="footer__descr">
              Copyright © 2023 Borsch. All rights reserved.
            </div>

            <ul className="footer__container">
              {footerArr.map(list => (
              <li 
                className="footer__list"
                key={list}
              >
                {list}
              </li>))}
            </ul>
      </div>
  );
}