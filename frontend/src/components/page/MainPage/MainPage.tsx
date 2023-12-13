import React, { useEffect, useState } from "react";
import "./MainPage.scss";
import { NavLink } from "react-router-dom";
import { HomePageLogic } from "../../pageComponents/HomePageLogic/HomePageLogic.tsx";
import { getStravi } from "../../../api.ts";
import { Stravi } from "../../../helpers/Stravi.tsx";
import { FilterBy } from "../../../helpers/FiltesedBy.tsx";

export const MainPage = () => {
    const [stravi, setStravi] = useState<Stravi[]>([]);
    const region = [
      'Galicia',
      'Slobozhanshchyna',
      'South',
      'Polissya',
      'Carpathians',
      'Podillya',
    ];

    useEffect(() => {
        getStravi()
          .then((straviFromServer) => {
            setStravi(straviFromServer);
          })
      }, []);

    return (
        <div className="main">
            <div className="main__region">
                <div className="main__region--text">
                    Discover the Flavors, Savor the History
                    <p className="main__region--arrow" />
                </div>
                
                <ul className="main__region--container">
                  {region.map((reg) => (
                  <li key={reg}>
                    <NavLink 
                      to={reg.toLowerCase()}
                      className="main__region--link"
                    >
                      {reg}
                    </NavLink>
                  </li>
                  ))}
                </ul>
            </div>
                <HomePageLogic 
                  stravi={stravi}
                  filter={FilterBy.Soup}
                  header={'Unesco on the Plate'}
                  descr="Explore the diversity of borsch - a true cultural heritage of Ukraine recognized by UNESCO. From classic red borscht to unique regional recipes. Immerse yourself in the flavorful world and history of this beloved Ukrainian dish!"
                />

                <HomePageLogic 
                  stravi={stravi}
                  filter={FilterBy.Bread}
                  header={'The menu of the unbroken'}
                  descr="Amidst the invasion, Ukrainians cherished the essence of freedom and life.
                  Our vision for victory includes a feast featuring Crimean yantiks, Mariupol fish soup, Mykolaiv-style yushka, Lviv syrnyk, Luhansk meat roll, Poltava tasty galushky, Kherson zucchini caviar, and more. Today, it's the unbroken's menu, soon to be the victors'!"
                />

                <HomePageLogic 
                  stravi={stravi}
                  filter={FilterBy.Rating}
                  header={'The menu of the unbroken'}
                  descr="This is an attempt to depict the horrifying reality Ukrainians faced during the artificially induced famine of 1932-33 and continue to endure amid Russia's full-scale war on Ukraine. The Holodomor is the story of every Ukrainian family."
                />
        </div>
    );
}