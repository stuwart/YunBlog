import axios from "axios";

export default async function getData(info, route, args) {
    try {
        const response = await axios.get(route);
        info.value = response.data;
        
    } catch (error) {
        console.error("存在错误:", error);
    }

}