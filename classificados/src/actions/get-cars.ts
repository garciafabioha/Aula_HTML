"use server"

import { getAllCars } from "@/services/car";

export const getCars = async () => {
    const cars = await getAllCars();
    return cars;
}