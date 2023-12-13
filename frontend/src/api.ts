import { Stravi } from "./helpers/Stravi";
import dishesData from "../src/stravi.json";

function wait(delay: number) {
  return new Promise(resolve => setTimeout(resolve, delay));
}

export async function getStravi(): Promise<Stravi[]> {
  return wait(500)
    .then(() => {
      const jsonData = dishesData as Stravi[];
      return Promise.resolve(jsonData);
    });
}