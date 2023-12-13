import { FilterBy } from "./FiltesedBy.tsx";
import { Stravi } from "./Stravi";

export const getFilteredStravi = (
    straviList: Stravi[],
    filterBy: FilterBy,
  ): Stravi[] => {
    const filteredArray = straviList.filter((stravi) => {
      switch (filterBy) {
        case FilterBy.Rating:
          return stravi.rating;
  
        case FilterBy.Bread:
          return stravi.category.toLowerCase().includes('bread');

          case FilterBy.Soup:
            return stravi.category.toLowerCase().includes('soup'); 
  
        default:
          return true;
      }
    });
    
    return filteredArray;
};