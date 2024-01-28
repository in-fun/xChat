import Wrapper from "@/components/PageWrapper";
import Sidebar from "@/containers/Sidebar";
import ChatWindow from "@/containers/ChatWindow";
import { useState } from "react";
import Head from "next/head";

export default function App() {
  const [botTitle, setBotTitle] = useState("");

  return (
    <>
      <Head>
        <title>{botTitle}</title>
      </Head>
      <Sidebar />
      <Wrapper>
        <ChatWindow
          setBotTitle={setBotTitle}
        />
      </Wrapper>
    </>
  );
}
