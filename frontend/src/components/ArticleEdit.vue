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
      <div class="markdownText" v-html="markdownText"></div>
      <el-form-item>
        <div class="button">
          <el-button round @click="goBack">取消</el-button>
          <el-button type="danger" round v-if="id != 0" @click="deleteArticle"
            >删除</el-button
          >
          <el-button type="primary" round @click="onSubmit">保存</el-button>
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import axios from "axios";
import { marked } from "marked";
import { onMounted, ref, reactive, watchEffect } from "vue";
import { useRoute } from "vue-router";
import router from "@/router";

const route = useRoute();
const id = route.params.id;

const form = reactive({
  title: "",
  tags: [],
  body: "",
});

const data = ref({});
const url = "/api/article/" + id + "/";
const markdownText = ref("");
watchEffect(() => {
  markdownText.value = marked(form.body);
});

const fetData = async () => {
  try {
    if (id != 0) {
      const response = await axios.get(url);
      data.value = response.data;
      form.title = data.value.title;
      form.tags = data.value.tags;
      form.body = data.value.body;
    }
  } catch (error) {
    console.log("存在错误：", error);
  }
};

const onSubmit = async () => {
  try {
    if (typeof form.tags === "string") form.tags = form.tags.split("，");
    if (id == 0) {
      const response = await axios.post("/api/article/", form);
    } else {
      const response = await axios.patch(url, form);
    }
    router.replace("/usercenter/admin-article/");
  } catch (error) {
    console.log("存在错误：", error);
  }
};

const goBack = () => {
  router.go(-1);
};

const deleteArticle = async() => {
    await axios.delete(url);
    router.replace("/usercenter/admin-article/");
};

onMounted(fetData);
</script>

<style lang="scss" scoped>
.edit {
  position: absolute;
  left: 80px;
  top: 60px;
  width: 100%;
  height: 100%;

  .button {
    margin-top: 100px;
  }
}
</style>