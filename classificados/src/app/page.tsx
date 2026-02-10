import { getCars } from "@/actions/get-cars";
import { Header } from "../components/header";
import { CarItem } from "@/components/car-item";

export default async function Page() {
  const cars = await getCars();

  return (
    <div>
      <Header />  

      <section className="grid sm:grid-cols-2 md:grid-cols-4 gap-4">
        {cars.map(carItem => (
          <CarItem key={carItem.id} data={carItem}/> 
        ))}                                       
      </section>
    </div>
  )
}


