import axios from "axios";
import { onMounted } from "vue";

export default function getData(info,url){
    const fetchData = async()=>{
        try{
            const response = await axios.get(url);
            info.value =response.data.results;
        }catch(error){
            console.error("存在错误:",error);
        }
    }
    fetchData();
}