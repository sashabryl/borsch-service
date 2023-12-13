import React from "react";
import { Stravi } from "../../../helpers/Stravi";
import { NavLink } from "react-router-dom";
import "./StraviCard.scss";

type Props = {
  stravi: Stravi,
}

export const StraviCard: React.FC<Props> = ({ stravi }) => {
      return (
          <NavLink to='/' className="card">
              <div className="card__top">
                  <div className="card__img">
                    <button className="card__like" />
                  </div>
              </div>

              <div className="card__header">
                  <h1 className="card__name">{stravi.name}</h1>
                  <p className="card__category">{stravi.category}</p>
              </div>

              <h2 className="card__descr">{stravi.description}</h2>
          </NavLink>
      );
  }