import Wrapper from "@/components/PageWrapper";
import Sidebar from "@/containers/Sidebar";
import Head from "next/head";
import CreateBot from "@/components/dashboard/CreateBot";

export default function App() {

  return (
    <>
      <Head>
        <title>Create Bot</title>
      </Head>
      <Sidebar />
      <Wrapper>
        <CreateBot/>
      </Wrapper>
    </>
  );
}
