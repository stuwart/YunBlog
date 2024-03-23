<template>
  <div class="edit">
    <el-form :model="form" label-width="auto" style="max-width: 600px">
      <el-form-item label="标题">
        <el-input v-model="form.title" />
      </el-form-item>
      <el-form-item label="标签">
        <el-input v-model="form.tags" />
      </el-form-item>
      <el-form-item label="文章内容">
        <el-input v-model="form.body" type="textarea" />
      </el-form-item>
      <el-form-item>
        <div class="button">
          <el-button round>取消</el-button>
          <el-button type="primary" round @click="onSubmit">保存</el-button>
          <el-button type="danger" round>删除</el-button>
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref, reactive } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const id = route.params.id;
const url = "/api/article/" + id + "/";

const form = reactive({
  title: "",
  tags: [],
  body: "",
});

const data = ref({});

const fetData = async () => {
  try {
    const response = await axios.get(url);
    data.value = response.data;
    // console.log(data.value);
    form.title = data.value.title;
    form.tags = data.value.tags;
    form.body = data.value.body;
  } catch (error) {
    console.log("存在错误：", error);
  }
};

const onSubmit = () => {
  console.log("success");
};

onMounted(fetData);
</script>

<style lang="scss" scoped>
</style>