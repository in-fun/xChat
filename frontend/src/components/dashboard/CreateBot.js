import { useState } from "react";
import { useRouter } from "next/router";

export default function CreateBot() {
  const [botName, setBotName] = useState("");
  const [status, setStatus] = useState("");
  const [config, setConfig] = useState(undefined);
  const router = useRouter();

  const handleCreateBot = async (e) => {
    e.preventDefault();
    const data = {
      name: botName,
      config
    };

    const response = await fetch("/api/create_bot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const botSlug = botName.toLowerCase().replace(/\s+/g, "_");
      router.push(`/${botSlug}/chat`);
    } else {
      setBotName("");
      setStatus("fail");
      setTimeout(() => {
        setStatus("");
      }, 3000);
    }
  };

  return (
    <>
      <div className="w-full">
        {/* Create Bot */}
        <form onSubmit={handleCreateBot}>
          <div className="border-b border-gray-900/10 pb-12">
            <h2 className="text-base font-semibold leading-7 text-gray-900">Create Bot</h2>
            <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              <div className="sm:col-span-4">
                <label htmlFor="name" className="block text-sm font-medium leading-6 text-gray-900">
                  Bot Name
                </label>
                <div className="mt-2">
                  <input
                    type="text"
                    name="name"
                    id="name"
                    autoComplete="name"
                    className="rounded-md shadow-sm border-0 ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
                    placeholder="Bot"
                    value={botName}
                    onChange={(e) => setBotName(e.target.value)}
                  />
                </div>
              </div>

              <div className="col-span-full">
                <label htmlFor="config" className="block text-sm font-medium leading-6 text-gray-900">
                  Config (YAML)
                </label>
                <div className="mt-2">
                  <textarea
                    id="config"
                    name="config"
                    rows={15}
                    className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                    value={config}
                    onChange={(e) => setConfig(e.target.value)}
                  />
                </div>
                <p className="mt-3 text-sm leading-6 text-gray-600">
                  For advanced usage, write it carefully.
                </p>
              </div>

              <div className="flex items-center justify-start gap-x-6">
                <button
                  type="submit"
                  className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                >
                  Submit
                </button>
              </div>

              {status === "fail" && (
                <div className="text-red-600 text-sm font-bold py-1">
                  An error occurred while creating your bot!
                </div>
              )}
            </div>
          </div>
        </form>
      </div>
    </>
  );
}
