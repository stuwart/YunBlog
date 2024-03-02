import axios from "axios";
import { watch, watchEffect, ref } from "vue";

export default async function getData(info, route, kwargs, totalPage) {
    try {
        // console.log("GETurl:", route);
        const response = await axios.get(route);
        info.value = response.data.results;
        // console.log(info.value);

        const pages = Math.ceil(response.data.count / 5);
        totalPage.value = pages; 
    } catch (error) {
        console.error("存在错误:", error);
    }

}