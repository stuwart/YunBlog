import axios from "axios";


export default function getData(info, url, kwargs) {
    const fetchData = async () => {
        try {
            const response = await axios.get(url);
            info.value = response.data.results;
        } catch (error) {
            console.error("存在错误:", error);
        }
    }
    fetchData();
}